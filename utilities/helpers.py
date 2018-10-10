
def wait_and_click(self, locator, number, locator_type):
    element = self.is_element_visible(locator.format(number), locator_type)
    self.click_on_returned_element(element)
