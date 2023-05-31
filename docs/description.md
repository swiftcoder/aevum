Aevum is a simple experimental programming language designed to test out language features - it is not a full-featured general purpose language, and it lacks many features as a result.

Let's look at a simple program in Aevum:
```
use std::{input::keyboard::{key_down, Key}, time::{now, instant, Duration}};

state GameState {
    last_frame_time: Instant,
    frame_delta: Duration,
    walking: boolean,
    position: f32,
}

fn handle_input {
    GameState.walking = key_down(Key.W);
}

fn update_state {
    if GameState.walking {
        GameState.position += 2.0 * GameState.frame_delta;
    }
}

fn main {
    GameState.last_frame_time = now();
    GameState.frame_delta = Duration(1.0 / 60.0);

    loop {
        handle_input();

        update_state();

        draw();

        GameState.frame_delta = GameState.last_frame_time - now();
        GameState.last_frame_time = now();
    }
}

```
