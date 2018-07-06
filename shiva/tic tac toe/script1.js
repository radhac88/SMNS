    var cell;
    var symbol = "X";

    function mark(cell) {
        if (cell.value == "     ") {
            cell.value = symbol;
            if (symbol == "X" ) symbol = "O";
            else symbol = "X";
        }
        if (winning_condition(cell.value)) {
            alert("You win!");
            return;
        } else if (!winning_condition(cell.value)) {
        } else {
            alert("Draw!")
        }
    }

    function winning_condition(symbol) {
        if (document.f1.b1.value == symbol && document.f1.b2.value == symbol && document.f1.b3.value == symbol) return true;
        else if (document.f1.b4.value == symbol && document.f1.b5.value == symbol && document.f1.b6.value == symbol) return true;
        else if (document.f1.b7.value == symbol && document.f1.b8.value == symbol && document.f1.b9.value == symbol) return true;
        else if (document.f1.b1.value == symbol && document.f1.b4.value == symbol && document.f1.b7.value == symbol) return true;
        else if (document.f1.b2.value == symbol && document.f1.b5.value == symbol && document.f1.b8.value == symbol) return true;
        else if (document.f1.b3.value == symbol && document.f1.b6.value == symbol && document.f1.b9.value == symbol) return true;
        else if (document.f1.b1.value == symbol && document.f1.b5.value == symbol && document.f1.b9.value == symbol) return true;
        else if (document.f1.b3.value == symbol && document.f1.b5.value == symbol && document.f1.b7.value == symbol) return true;
        else return false;
    }

    function resetGame() {
        status = "X"
        document.f1.b00.value = "   ";
        document.f1.b01.value = "   ";
        document.f1.b02.value = "   ";
        document.f1.b10.value = "   ";
        document.f1.b11.value = "   ";
        document.f1.b12.value = "   ";
        document.f1.b20.value = "   ";
        document.f1.b21.value = "   ";
        document.f1.b22.value = "   ";
    }