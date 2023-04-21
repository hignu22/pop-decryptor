struct Counter {
    timeline: Timeline
}

// ~ SNIP

impl Application for Counter {
  // ~ SNIP
   fn new(_flags: ()) -> (Self, Command<Message>) {
      (Self { timeline: Timeline::new()}, Command::none())
   }
}
