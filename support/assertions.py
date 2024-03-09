class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, f"Actual:{actual} not equal to Expected:{expected}"
