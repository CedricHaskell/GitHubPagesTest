---
title: 小游戏 Demo
description: 以复古贪吃蛇为例，说明如何在页面中嵌入交互式 HTML/JS 组件。
---

# 小游戏 Demo

`md_in_html` 扩展会把任意 HTML、CSS 与 JavaScript 原样传递到页面。这让讲义具备交互性：练习可以是测验、模拟器或直接运行在浏览器中的游戏。

下面的贪吃蛇游戏内嵌于本页，不使用任何外部代码。代码刻意保持精简——一个 canvas、一个循环——以便看清机制。用方向键（或 W/A/S/D）控制方向。

## 演示

<div id="snake-game"
     data-label-score="得分"
     data-label-restart="重新开始"
     data-label-over="游戏结束——得分 {score}。"></div>

<style>
  #snake-game { position: relative; width: 320px; max-width: 100%; background: #000; border: 2px solid #33ff33; padding: 12px; font-family: monospace; color: #33ff33; }
  .snake-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
  .snake-bar span { text-transform: uppercase; font-size: 0.9rem; }
  .snake-btn { background: #000; color: #33ff33; border: 1px solid #33ff33; padding: 2px 8px; font-family: inherit; font-size: 0.9rem; text-transform: uppercase; cursor: pointer; }
  .snake-btn:hover { background: #33ff33; color: #000; }
  .snake-board { display: block; border: 1px solid #33ff33; }
  .snake-win { position: absolute; inset: 0; background: #000; border: 2px solid #33ff33; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; text-align: center; padding: 8px; }
  .snake-win p { margin: 0; }
</style>

<script>
  (function () {
    "use strict";

    var root = document.getElementById("snake-game");
    if (!root) return;

    var L = {
      score: root.dataset.labelScore || "Score",
      restart: root.dataset.labelRestart || "New game",
      over: root.dataset.labelOver || "Game over — score {score}."
    };

    var CELL = 16;   // board cell size in px
    var N = 20;      // board is N by N cells
    var TICK = 120;  // ms per game step

    var bar = document.createElement("div");
    bar.className = "snake-bar";
    var scoreEl = document.createElement("span");
    var restartBtn = document.createElement("button");
    restartBtn.type = "button";
    restartBtn.className = "snake-btn";
    restartBtn.textContent = "[ " + L.restart + " ]";
    bar.appendChild(scoreEl);
    bar.appendChild(restartBtn);

    var canvas = document.createElement("canvas");
    canvas.className = "snake-board";
    canvas.width = N * CELL;
    canvas.height = N * CELL;
    root.appendChild(bar);
    root.appendChild(canvas);
    var ctx = canvas.getContext("2d");

    var snake, dir, nextDir, food, score, timer, dead;

    function render() {
      scoreEl.textContent = L.score + ": " + score;
    }

    function placeFood() {
      do {
        food = { x: Math.floor(Math.random() * N), y: Math.floor(Math.random() * N) };
      } while (snake.some(function (s) { return s.x === food.x && s.y === food.y; }));
    }

    function draw() {
      ctx.fillStyle = "#000";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      // the food: a hollow square
      ctx.strokeStyle = "#33ff33";
      ctx.strokeRect(food.x * CELL + 3, food.y * CELL + 3, CELL - 6, CELL - 6);
      // the snake: filled squares
      ctx.fillStyle = "#33ff33";
      snake.forEach(function (s) {
        ctx.fillRect(s.x * CELL + 1, s.y * CELL + 1, CELL - 2, CELL - 2);
      });
    }

    function step() {
      dir = nextDir;
      var head = snake[0];
      var nx = head.x + dir.x;
      var ny = head.y + dir.y;
      if (nx < 0 || ny < 0 || nx >= N || ny >= N) return gameOver();
      var grow = nx === food.x && ny === food.y;
      // self collision; the tail cell is safe when not growing
      var limit = grow ? snake.length : snake.length - 1;
      for (var i = 0; i < limit; i++) {
        if (snake[i].x === nx && snake[i].y === ny) return gameOver();
      }
      snake.unshift({ x: nx, y: ny });
      if (grow) {
        score++;
        render();
        placeFood();
      } else {
        snake.pop();
      }
      draw();
    }

    function gameOver() {
      clearInterval(timer);
      timer = null;
      dead = true;
      var overlay = document.createElement("div");
      overlay.className = "snake-win";
      var p = document.createElement("p");
      p.textContent = L.over.replace("{score}", score);
      overlay.appendChild(p);
      var again = document.createElement("button");
      again.type = "button";
      again.className = "snake-btn";
      again.textContent = "[ " + L.restart + " ]";
      again.addEventListener("click", reset);
      overlay.appendChild(again);
      root.appendChild(overlay);
    }

    function reset() {
      var overlay = root.querySelector(".snake-win");
      if (overlay) overlay.remove();
      clearInterval(timer);
      snake = [{ x: 10, y: 10 }, { x: 9, y: 10 }, { x: 8, y: 10 }];
      dir = { x: 1, y: 0 };
      nextDir = dir;
      score = 0;
      dead = false;
      placeFood();
      render();
      draw();
      timer = setInterval(step, TICK);
    }

    document.addEventListener("keydown", function (e) {
      if (dead) return;
      var d = null;
      if (e.key === "ArrowUp" || e.key === "w") d = { x: 0, y: -1 };
      if (e.key === "ArrowDown" || e.key === "s") d = { x: 0, y: 1 };
      if (e.key === "ArrowLeft" || e.key === "a") d = { x: -1, y: 0 };
      if (e.key === "ArrowRight" || e.key === "d") d = { x: 1, y: 0 };
      if (!d) return;
      e.preventDefault();
      if (d.x === -dir.x && d.y === -dir.y) return;  // no 180-degree turns
      nextDir = d;
    });

    restartBtn.addEventListener("click", reset);
    reset();
  })();
</script>

## 工作原理

组件由三部分组成，全部直接写在 Markdown 文件中：

1. **容器** —— 一个空的 `<div id="snake-game">`。它的 `data-*` 属性承载所有可见文字（得分、重新开始、结束提示）。脚本在启动时读取这些属性，因此同一份代码服务两种语言：本页的中文版传入中文标签，代码完全一致。
2. **样式** —— 一个作用于组件的 `<style>` 块。外观刻意采用极简复古终端风格：黑底绿字、等宽字体、硬直角边框、无动画。组件使用自己的固定配色而不跟随站点主题；另一种做法是使用 Material 的 CSS 变量（`--md-primary-fg-color`、`--md-code-bg-color` 等）让组件跟随主题与明暗模式。
3. **脚本** —— 一个自包含的 IIFE，在 canvas 上绘制棋盘，用 `setInterval` 驱动游戏循环，读取键盘输入并渲染得分。无任何库、无构建步骤。

结束提示中的 `{score}` 占位符会被脚本替换为实际得分。

## 把代码抽取到共享文件

出现在多个页面上的组件不应重复复制。生产化的形式是：容器留在页面中，样式与脚本移入只加载一次的共享文件：

1. 把 CSS 与 JS 移入 `docs/assets/js/my-widget.js`（JS 自行创建 `<style>` 元素；或把 CSS 放入 `docs/assets/css/` 并通过 `extra_css` 加载）。
2. 全局注册脚本：

    ```yaml
    extra_javascript:
      - assets/js/my-widget.js
    ```

3. 使用守卫式初始化，让脚本在缺少容器的页面上什么都不做：

    ```js
    document.addEventListener("DOMContentLoaded", function () {
      var root = document.getElementById("my-widget");
      if (root) initMyWidget(root);
    });
    ```

模板自带的 `mathjax.js` 用的就是这一模式。配置细节见[自定义](customization.md)。

## 讲义中的用法

- 带得分与 `localStorage` 跨会话记忆的测验。
- 词汇或命令的闪卡。
- 通过 CodePen 或 Replit 的 `<iframe>` 内嵌代码运行器，用于编程练习。
- 用少量按钮与 canvas 实现的小型模拟器（例如算法可视化）。

## 注意事项

- 组件保持零依赖、体积小；它们随每次访问加载。
- 在两种语言版本上都测试组件——所有可见文字都应来自容器的 `data-*` 属性。
- 交互代码运行在访问者的浏览器中，不要嵌入密钥或 API key。
- 脚本与样式块被 Markdown 解析器视为原始内容；避免写出可能被误认为标记的字符串（例如脚本中出现字面的 `</script>`）。
- 棋盘绘制在 canvas 上，屏幕阅读器无法读取；正式使用时，应在周围文字中说明操作方式。
