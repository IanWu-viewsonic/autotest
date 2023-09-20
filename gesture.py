"""Gesture Class."""
import subprocess
import cv2
import numpy as np
from logger import Logger


class Gesture:
    # define gesture

    def __init__(self, driver) -> None:
        self.logger = Logger()
        if not driver:
            raise ValueError('driver can not be null.')
        self.driver = driver

    def open_activity(self, element) -> None:
        package = element[0]
        activity = element[1]
        self.driver.app_start(package, activity)

    def tap(self, element) -> None:
        # Tap function
        element.click()

    def tap_image(self, element) -> None:
        self.driver.image.click(element)

    def zoom_in(self, element=None) -> None:
        if element is None:
            element = self.driver()
        element.pinch_out(percent=10, steps=10)

    def zoom_out(self, element=None) -> None:
        if element is None:
            element = self.driver()
        element.pinch_in(percent=10, steps=10)

    def send_keys(self, element, keyword) -> None:
        element.send_keys(keyword)

    def clear_keys(self, element) -> None:
        element.clear_text()

    def double_tap(self, element) -> None:
        # double tap function
        element.double_click()

    def back(self) -> None:
        # back button
        self.driver.keyevent("back")

    def screenshot(self, save_location) -> None:
        # screenshot current screen
        self.driver.screenshot(save_location)

    def double_finger(self) -> None:
        # double_finger use
        pass

    def long_press_element(self, element) -> None:
        # long_press fuction
        element.long_click(duration=2)

    def long_press_location(self, location_x, location_y):
        self.driver.long_click(x=location_x, y=location_y, duration=2)

    def home_page(self) -> None:
        # home page button
        self.driver.keyevent("home")

    def overview_page(self) -> None:
        # overview button
        self.driver.keyevent("overview")

    def quit_driver(self) -> None:
        # quit driver
        self.driver.quit()

    def current_app(self) -> None:
        # get current app
        return self.driver.app_current()

    def swipe_left(self, element=None) -> None:
        # swipe left function
        if element is None:
            element = self.driver()
        element.swipe("left")

    def swipe_right(self, element=None) -> None:
        # swipe left function
        if element is None:
            element = self.driver()
        element.swipe("right")

    def swipe_up(self, element=None) -> None:
        # Swipe up function
        if element is None:
            element = self.driver()
        element.swipe("up")

    def swipe_down(self, element=None) -> None:
        # Swipe up function
        if element is None:
            element = self.driver()
        element.swipe("down")

    def drag_element_screen(self, element, horizontal, vertical) -> None:
        '''Default is upper right corner'''
        element_bounds = element.info['bounds']
        # center x,y is element center , target x , y is screen width , height
        center_x = (element_bounds['left'] + element_bounds['right']) // 2
        center_y = (element_bounds['top'] + element_bounds['bottom']) // 2

        if horizontal is None:
            # 屏幕的宽度减 1，即最右侧的位置
            horizontal = self.driver.info['displayWidth'] - 1
        if vertical is None:
            vertical = 0

        self.driver.drag(center_x, center_y, horizontal, vertical)

    def install_app(self, element) -> None:
        command = ['adb', 'install', "-r", element]
        subprocess.run(command, check=False)

    def uninstall_app(self, element) -> None:
        command = ['adb', 'uninstall', element]
        subprocess.run(command, check=False)

    def get_overview_activities(self) -> None:
        result = subprocess.check_output(
            ["adb", "shell", "dumpsys", "activity", "recents"], universal_newlines=True)
        lines = result.split("\n")
        activities = []
        activities = [line.split(
        )[2] for line in lines if "ActivityRecord" in line and len(line.split()) >= 4]
        return activities

    def check_background_activities(self, element) -> None:
        # check background activities match the app or not
        overview_activities = self.get_overview_activities()
        activity_list = []
        if overview_activities:
            activity_list.extend(overview_activities)
            if any(element in background for background in activity_list):
                self.logger.info(f"{element} is in the background")
            else:
                self.logger.error(f"{element} is not in the background")
        else:
            self.logger.error("No overview activities found.")

    def compare_images_pixel(self, compare_1, compare_2) -> None:
        # read two pictures
        img1 = cv2.imread(compare_1)
        img2 = cv2.imread(compare_2)

        # compare all pixel different
        diff_image = cv2.absdiff(img1, img2)
        diff_pixels = np.sum(diff_image, axis=2)  # count different pixel
        different_pixel_count = np.count_nonzero(diff_pixels)
        if different_pixel_count > 3000:
            pass

        else:
            self.logger.error('compare different fail')

    def clean_activity(self, element):
        command = ['adb', 'shell', 'pm', 'clear', element]
        subprocess.run(
            command, capture_output=True, text=True, check=True)

    def update_file(self, element):
        command = ['adb', 'push', element, '/sdcard/']
        subprocess.run(command, check=False)

    def delete_file(self, element):
        command = ['adb', 'shell', 'rm', '/sdcard/', element]
        subprocess.run(command, shell=True, capture_output=True,
                       text=True, check=False)

    def reboot(self):
        command = ['adb', 'reboot']
        subprocess.run(command, check=True)

    def wait_for_device(self):
        command = ['adb', 'wait-for-device']
        subprocess.run(command, check=True)

    def close_app(self, element):
        self.driver.app_stop(element)
