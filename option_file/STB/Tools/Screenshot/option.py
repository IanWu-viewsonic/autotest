"""Screenshot test case"""
import item_strategy


class Screenshot(item_strategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "crop",
        "2": "full screen",
        "3": "save",
        "4": "close",
        "all": "all Test",
    }
    folder_path = "option_file/STB/Tools/Screenshot"

    def __init__(self, event_gen, driver, html_report):
        super().__init__(event_gen, driver, html_report)

    def _STB_screenshot_crop(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_screenshot_crop.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB Screenshot-crop")

    def _STB_screenshot_full_screen(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_screenshot_full_screen.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB Screenshot-full screen")

    def _STB_screenshot_save(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_screenshot_save.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB Screenshot-save")

    def _STB_screenshot_close(self):
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_screenshot_close.json",
            driver=self.driver,
        )
        self.html_report.report_data["category"] = "STB"
        self.html_report.test_case("STB Screenshot-close")

    def run_all(self):
        self.html_report.test_title("---STB Tool - Screenshot---")
        self._STB_screenshot_crop()
        self._STB_screenshot_full_screen()
        self._STB_screenshot_save()
        self._STB_screenshot_close()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_screenshot_crop()
                case "2":
                    self._STB_screenshot_full_screen()
                case "3":
                    self._STB_screenshot_save()
                case "4":
                    self._STB_screenshot_close()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
