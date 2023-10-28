CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_position = 1

    def first_channel(self):
        self.current_position = 1
        return self.channels[self.current_position - 1]

    def last_channel(self):
        self.current_position = len(self.channels)
        return self.channels[self.current_position - 1]

    def turn_channel(self, channel_number):
        if 1 <= channel_number <= len(self.channels):
            self.current_position = channel_number
            return self.channels[self.current_position - 1]
        else:
            return "No exist"

    def next_channel(self):
        self.current_position = (self.current_position % len(self.channels)) + 1
        return self.channels[self.current_position - 1]

    def previous_channel(self):
        self.current_position = (self.current_position - 2) % len(self.channels) + 1
        return self.channels[self.current_position - 1]

    def current_channel(self):
        return self.channels[self.current_position - 1]

    def exists(self, channel):
        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"


controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.exists(4))
print(controller.exists("BBC"))

