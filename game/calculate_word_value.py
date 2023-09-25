from game.cell import Cell

class CalculateWordValue:
    @staticmethod
    def calculate_word_value(word):
        value = 0
        multiplier_word = 1
        all_cells_inactive = True  # Bandera para verificar si todas las celdas están inactivas

        for cell in word:
            cell_value = cell.calculate_value()
            if cell.multiplier_type == 'word':
                multiplier_word *= cell.multiplier
            value += cell_value

            # Verificar si la celda está activa
            if cell.active:
                all_cells_inactive = False

        # Si todas las celdas están inactivas, el valor es 0
        if all_cells_inactive:
            return 0

        value *= multiplier_word
        return value
