"""Timer test case"""
import ItemStrategy


class Timer(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "start and wait the bell",
        "2": "pause & resume & reset",
        "3": "expand",
        "all": "all Test",
    }
    folder_path = "Test_Jason/STB/Tools/Timer"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_timer_start_ring(self):
        self.logger.Test("STB timer-start to wait the bell ring")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_timer_start_ring.json",
            driver=self.driver,
        )

    def _STB_timer_pause_resume_reset(self):
        self.logger.Test("STB timer-pause & resume & reset button")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_timer_pause_resume_reset.json",
            driver=self.driver,
        )

    def _STB_timer_expand(self):
        self.logger.Test("STB timer-expand the timer window")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_timer_expand.json",
            driver=self.driver,
        )

    def run_all(self):
        self.logger.test_title("---STB Tool - Stopwatch---")
        self._STB_timer_start_ring()
        self._STB_timer_pause_resume_reset()
        self._STB_timer_expand()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_timer_start_ring()
                case "2":
                    self._STB_timer_pause_resume_reset()
                case "3":
                    self._STB_timer_expand()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
