# Altered output of ChatGPT

from unittest.mock import patch
from add_new import *

@patch("add_new.enter_details")
def test_add_new_with_valid_path(mock_enter_details):
    img_path = "../thumbnails/coats/hollister-parka.webp"

    # Call the add_new function with a valid image path
    result = add_new(img_path)

    # Assert that enter_details is called with the correct path
    mock_enter_details.assert_called_once_with(img_path)

    # Assert that the result is 0 (success)
    assert result == 0

@patch("add_new.enter_details")
def test_add_new_with_invalid_path(mock_enter_details):
    img_path = "invalid_path.jpg"

    # Call the add_new function with an invalid image path
    result = add_new(img_path)

    # Assert that enter_details is not called
    mock_enter_details.assert_not_called()

    # Assert that the result is 1 (failure)
    assert result == 1

# Test add_new when img_path is "t" (for testing purposes)
@patch("add_new.enter_details")
def test_add_new_testing_path(mock_enter_details):
    img_path = "t"
    
    # Call the add_new function with testing path
    result = add_new(img_path)
    
    # Assert that enter_details is called with the correct path
    mock_enter_details.assert_called_once_with('../thumbnails/coats/hollister-parka.webp')
    
    # Assert that the result is 0 (success)
    assert result == 0

def test_enter_details_failure():
    with patch('builtins.input', side_effect=["Brand", "Colour", "Shirt"]):
        with patch('add_new.enter_clothing_type_details', return_value=("Shirt", 1)):
            result = enter_details("img_path")

            assert isinstance(result, int)
            assert result == 1

def test_enter_details_new_clothing_item():
    with patch('builtins.input', side_effect=["Brand", "Colour", "Shirt"]):
        with patch('add_new.enter_clothing_type_details', return_value=("Shirt", 0)):
            with patch('os.rename'):
                result = enter_details("img_path")

                assert isinstance(result, int)
                assert result == 0

@patch('builtins.input', return_value="Shirt")  # Mocking input function
def test_enter_clothing_type_details_valid(mock_input):
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['Shirt', 'Pants', 'Shoes']

        result_type, result_status = enter_clothing_type_details()

        mock_input.assert_called_once_with(MSG_ENTER_CLOTHING_DETAILS.format(['Shirt', 'Pants', 'Shoes']))
        assert result_type == 'Shirt'
        assert result_status == 0

@patch('builtins.input', return_value="Hat")  # Mocking input function
def test_enter_clothing_type_details_invalid(mock_input):
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['Shirt', 'Pants', 'Shoes']

        result_type, result_status = enter_clothing_type_details()

        mock_input.assert_called_once_with(MSG_ENTER_CLOTHING_DETAILS.format(['Shirt', 'Pants', 'Shoes']))
        assert result_type == 'Hat'
        assert result_status == 1