from selenium import webdriver
import unittest


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
        pass


class TestPermissions(TestClass):
    def test_index_redirect(self):
        self.driver.get("http://localhost:5000/index")
        elem = self.driver.find_element_by_tag_name("h1")
        assert "Flask App" in self.driver.title
        assert elem.text == "Sign In"


class TestPages(TestClass):
    def test_index_signin(self):
        self.driver.get("http://localhost:5000/signin")
        elem = self.driver.find_element_by_tag_name("h1")
        assert "Flask App" in self.driver.title
        assert elem.text == "Sign In"

    def test_index_signup(self):
        self.driver.get("http://localhost:5000/signup")
        elem = self.driver.find_element_by_tag_name("h1")
        assert "Flask App" in self.driver.title
        assert elem.text == "Sign Up"


if __name__ == "__main__":
    unittest.main()
