# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.9] - 2023-10-22

### Changed

I redid the generate row string method within the Board class, added new tests to validate these lines (they still don't work). And also try to implement a new test inside test_scrabble.py

## [0.2.8] - 2023-10-19

### Added

Update with DockerFile

## [0.2.7] - 2023-10-18

### Changed

We fixed the get_player_count inside main and adjusted the tests so that they work correctly, we also made minimal changes to the other methods.

## [0.2.6] - 2023-10-17

### Changed

We changed the functions within main.py to improve the structure and to make it more readable. The most modified were: get_inputs and get_player_count for better validation and show_board to make the board look more readable.
(Errors need to be corrected within these changes)


## [0.2.5] - 2023-10-12

### Added

We added new methods within the Scrabble class: is_playing, get_current_player and get_horizontal_word

### Changed

It was necessary to change the get_words method within the Scrabble class

## [0.2.4] - 2023-10-09

### Added

On the other hand, complete the get_words method of the Scrabble class

### Changed

Update the main.py class, define the show_player function and modify get_playe_count next to show Board

## [0.2.3] - 2023-10-06

### Changed

I fixed what didn't work within the main function and created the show_board functions and in scrabble I added the calculate_words_value and dict_validate_word methods

## [0.2.2] - 2023-10-05

### Changed

Try to replace the main code that the teacher sent and his tests

## [0.2.1] - 2023-10-04

### Changed

Change the Board class from scratch, add new methods with cell multipliers, validate if the words are inside or outside the board, etc.

## [0.2.0] - 2023-10-01

### Added

We defined a new is_empty method inside the Board class but there are still problems with validating 2 tests

## [0.0.19] - 2023-09-27

### Added

We add a text file with all the words that the scrabble game can contain, we add a new class called Dictionary and together with it we create its tests.

## [0.0.18] - 2023-09-25

### Changed

We change def validate_word_place_board in the Board class and complete it with corresponding tests

## [0.0.17] - 2023-09-23

### Changed

We modify the calculate_word_value class and add new tests that correctly validate the modifications.

## [0.0.16] - 2023-09-18

### Added

We added the new tests test_calculate_word_value_with_no_multiplier, test_validate_word_out_of_board_horizontal_false, test_validate_word_inside_board_horizontal_false and modified some of the existing ones.

### Changed

We change calculate_word_value inside the Board class

## [0.0.15] - 2023-09-17

### Changed

Change the validate_word_place_board method of the Board class so that test_board tests are validated

## [0.0.14] - 2023-09-16

### Added

We define new methods to the board class to validate some of the tests performed in the class (test_validate_word_inside_board_vertical_valid, test_validate_word_out_of_board_horizontal_valid...)

## [0.0.13] - 2023-09-13

### Added

Within the board class we added new methods to corroborate the place of the words and together with these respective tests that do not work at the moment.

## [0.0.12] - 2023-09-12

### Added

We implement the new main class along with its valid_player_count, get_player_county play methods, and also with its tests.

## [0.0.11] - 2023-09-11

### Added

Defines the new methods worked in class and the verification of their correct functioning

## [0.0.10] - 2023-09-10

### Added

We added new tests for board and new methods to satisfy them (within the Board class

## [0.0.9] - 2023-09-09

### Changed

Editing and searching for correct functioning of test_scrabbleGame.

## [0.0.8] - 2023-09-07

### Added

Define the new Calculate_word_value class along with the calculate method. And from these perform a test_simple

### Changed

Generate a couple of modifications to the cell class for the correct function of calculate_word_value

## [0.0.7] - 2023-09-03

### Changed

Modify Cell, Player class and update commands inside codeclimate, circle and modify readme file

## [0.0.6] - 2023-08-29

### Added

Define the Scrabble class with a constructor and its respective tests

## [0.0.5] - 2023-08-29

### Added

Add new methods for the cell class and next to these their respective tests

## [0.0.4] - 2023-08-28

### Added

-I defined a new method inside the Player class called "get_score" and added to this its test in the TestPlayer class
-Add new methods for the Cell class (is_empty, has_letter, apply_word_multiplier and apply_letter_multiplier)
-I defined the Board class with a constructor and a Test

## [0.0.3] - 2023-08-27

### Added

We define the new Cell class with the add_letter and calculate_value methods.
Together with this we define their respective tests

## [0.0.2] - 2023-08-27

### Added

We define the MockCell classes that create a mock cell instance, and the Player class that contains the validate_word and pass_turn methods.
We also define their respective tests

## [0.0.1] - 2023-08-27

### Added

We define the Tiles and BagTiles classes, both with their constructors and in the BagTiles class we add the take and put methods.
In another separate file the corresponding tests were made
