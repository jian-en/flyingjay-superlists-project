# -*- coding: utf-8 -*-
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):

        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        self.get_item_input_box().send_keys('\n')

        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith 访问主页输入一个新的待办事项
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # 她无意中输入了一个重复的事项
        self.get_item_input_box().send_keys('Buy wellies\n')

        # 她看到了一条有用的错误信息
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Edith 没有输入待办事项，就直接敲击了回车键，发现错误信息出现了
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # 她开始敲击键盘打入a
        self.get_item_input_box().send_keys('a')

        # 她发现错误信息消失了
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
