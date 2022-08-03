class MyCalendar:

    def __init__(self):
        self.lst = []

    def book(self, start: int, end: int) -> bool:
        if self.lst == []:
            self.lst.append([start, end])
            return True
        for lts in self.lst:
            if start < lts[1] and end > lts[0]:
                return False
        self.lst.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)