import arcade


while True:
    input("Press enter to spin!")
    col1 = arcade.spin_column()
    col2 = arcade.spin_column()
    col3 = arcade.spin_column()
    arcade.draw_display(col1, col2, col3)

    tickets = str(arcade.get_score(col1, col2, col3))
    print(f"You won {tickets} tickets!")

    arcade.get_score("$", "$", "$")

    # Play Again!
    play_again = input('Would you like to play more? (Yes/No): ').capitalize()
    if play_again != "Yes":
        break