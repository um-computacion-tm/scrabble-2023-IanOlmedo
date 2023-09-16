# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
