use iced::{button, Button, Column, Element, Sandbox, Settings, Text};

struct App {
    counter: i32,
    increment_button: button::State,
    decrement_button: button::State,
}

#[derive(Debug, Clone, Copy)]
enum Message {
    IncrementPressed,
    DecrementPressed,
}

impl Sandbox for App {
    type Message = Message;

    fn new() -> Self {
        App {
            counter: 0,
            increment_button: button::State::new(),
            decrement_button: button::State::new(),
        }
    }

    fn title(&self) -> String {
        String::from("Rust Iced App")
    }

    fn update(&mut self, message: Message) {
        match message {
            Message::IncrementPressed => {
                self.counter += 1;
            }
            Message::DecrementPressed => {
                self.counter -= 1;
            }
        }
    }

    fn view(&mut self) -> Element<Message> {
        let increment_button = Button::new(&mut self.increment_button, Text::new("Increment"))
            .on_press(Message::IncrementPressed);
        let decrement_button = Button::new(&mut self.decrement_button, Text::new("Decrement"))
            .on_press(Message::DecrementPressed);

        Column::new()
            .spacing(20)
            .push(Text::new(format!("Counter: {}", self.counter)))
            .push(increment_button)
            .push(decrement_button)
            .into()
    }
}

fn main() {
    App::run(Settings::default());
}
}
