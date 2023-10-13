"""Freezer test case"""
import ItemStrategy


class Freezer(ItemStrategy.Strategy):
    menu_dict = {
        "0": "Back to main menu",
        "1": "Zoom in & out, by button",
        "2": "Zoom in & out, by fingers",
        "3": "Zoom in, button first than fingers",
        "4": "default screen button",
        "5": "reboot to freezer",
        "all": "all Test",
    }
    folder_path = "Test_Jason/STB/Tools/Freezer"

    def __init__(self, event_gen, logger, driver):
        super().__init__(event_gen, logger, driver)

    def _STB_freezer_zoom_in_out_button(self):
        self.logger.Test("STB Freezer-tap button to zoom in & zoom out")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_freezer_zoom_in_out_button.json",
            driver=self.driver,
        )

    def _STB_freezer_zoom_in_out_fingers(self):
        self.logger.Test("STB Freezer-use fingers to zoom in & zoom out")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_freezer_zoom_in_out_fingers.json",
            driver=self.driver,
        )

    def _STB_freezer_zoom_mix(self):
        self.logger.Test(
            "STB Freezer-use fingers to zoom in first than use button to zoom in"
        )
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_freezer_zoom_mix.json",
            driver=self.driver,
        )

    def _STB_freezer_default_button(self):
        self.logger.Test("STB Freezer-default screen button")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_freezer_default_button.json",
            driver=self.driver,
        )

    def _STB_freezer_reboot_to_use(self):
        self.logger.Test("STB Freezer-reboot the device and use freezer zoom in & out")
        self.event_gen.generate_event(
            json_path=f"{self.folder_path}/STB_freezer_reboot_to_use.json",
            driver=self.driver,
        )

    def run_all(self):
        self.logger.test_title("---STB Tool - Freezer---")
        self._STB_freezer_reboot_to_use()
        self._STB_freezer_zoom_in_out_button()
        self._STB_freezer_zoom_in_out_fingers()
        self._STB_freezer_zoom_mix()
        self._STB_freezer_default_button()

    def run(self):
        while True:
            for option, test in self.menu_dict.items():
                print(f"{option}: {test}")
            choice = input("Enter your choice: ").lower()
            match choice:
                case "0":
                    return
                case "1":
                    self._STB_freezer_zoom_in_out_button()
                case "2":
                    self._STB_freezer_zoom_in_out_fingers()
                case "3":
                    self._STB_freezer_zoom_mix()
                case "4":
                    self._STB_freezer_default_button()
                case "5":
                    self._STB_freezer_reboot_to_use()
                case "all":
                    self.run_all()
                case _:
                    print("Invalid option")
