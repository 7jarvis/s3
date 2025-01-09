from pages.dynamic_content_page import DynamicContent
import pytest


@pytest.mark.parametrize(
    "num_of_images, num_of_same_images_needed",
    [(3, 2)]

)
def test_dynamic_content(browser, config, num_of_images, num_of_same_images_needed):
    browser.get(config.get_value("test10_url"))
    dynamic = DynamicContent(browser)
    dynamic.wait_for_open()
    while len(set(dynamic.compare_images(num_of_images))) > num_of_same_images_needed:
        browser.refresh()
