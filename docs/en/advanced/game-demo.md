---
title: Game Demo
description: How to embed an interactive mini-game in a page, as an example of custom HTML/JS widgets.
---

# Game Demo

The `md_in_html` Markdown extension passes arbitrary HTML, CSS, and JavaScript through to the page. This makes worksheets interactive: exercises can be quizzes, simulators, or games that run directly in the browser.

The Snake game below is embedded in this page and uses no external code. It is deliberately small — one canvas, one loop — so the mechanism stays visible. Use the arrow keys (or W/A/S/D) to steer.

## The demo

<div id="snake-game"
     data-label-score="Score"
     data-label-restart="New game"
     data-label-over="Game over — score {score}."></div>

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

## How it works

The widget has three parts, all written directly in the Markdown file:

1. **The container** — an empty `<div id="snake-game">`. Its `data-*` attributes carry every visible label (score, restart, game-over message). The script reads them at startup, so the same code serves both languages: the Chinese version of this page passes Chinese labels, the code is identical.
2. **The styles** — a `<style>` block scoped to the widget. The look is deliberately a minimal retro terminal: green-on-black, monospace, hard square borders, no animations. The widget uses its own fixed palette instead of the site theme; the alternative is to use Material's CSS variables (`--md-primary-fg-color`, `--md-code-bg-color`, …) so a widget follows the theme and dark mode.
3. **The script** — a self-contained IIFE that draws the board on a canvas, runs the game loop with `setInterval`, reads the keyboard, and renders the score. No libraries, no build step.

The `{score}` placeholder in the game-over message is replaced by the script with the actual score.

## Extracting the code into a shared file

A widget that appears on several pages should not be duplicated. The production form keeps the container in the page and moves the styles and script to a shared file loaded once:

1. Move the CSS and JS into `docs/assets/js/my-widget.js` (the JS creates the `<style>` element itself, or the CSS goes to `docs/assets/css/` and is loaded via `extra_css`).
2. Register the script globally:

    ```yaml
    extra_javascript:
      - assets/js/my-widget.js
    ```

3. Use a guarded initializer so the script does nothing on pages without the container:

    ```js
    document.addEventListener("DOMContentLoaded", function () {
      var root = document.getElementById("my-widget");
      if (root) initMyWidget(root);
    });
    ```

This is the pattern used by the template's own `mathjax.js`. See [Customization](customization.md) for the configuration details.

## Ideas for worksheets

- A quiz with a score and `localStorage` persistence between sessions.
- Flashcards for vocabulary or commands.
- An embedded code runner via a CodePen or Replit `<iframe>` for programming exercises.
- A small simulator (e.g. visualizing an algorithm) with a few buttons and a canvas.

## Notes

- Keep widgets dependency-free and small; they load on every visit.
- Test the widget on both language versions — all visible text should come from the container's `data-*` attributes.
- Interactive code runs in the visitor's browser. Do not embed secrets or API keys.
- Script and style blocks are treated as raw content by the Markdown parser; avoid writing strings that could be mistaken for markup (e.g. a literal `</script>` inside the script).
- The board is drawn on a canvas, which screen readers cannot read; in production, describe the controls in the surrounding text.
