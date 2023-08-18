import tkinter as tk
from PIL import Image, ImageTk
from deck import Deck
from player import Player


root = tk.Tk()
root.title('Simple TK cardgame')
root.geometry("900x500")
root.configure(background="green")

def resize_cards(card):
	our_card_img = Image.open(card)
	our_card_resize_image = our_card_img.resize((150, 218))
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)
	return our_card_image

def startGame():

	deck.build()
	deck.shuffle()

	root.title(f'{len(deck)} Cards Left')
	player1_status_label.config(text='')
	player2_status_label.config(text='')

	player1.draw(deck)
	player2.draw(deck)

	global temp_image1
	temp_image1 = resize_cards(f'images/{player1.currentCard}.png')
	player1_label.config(image=temp_image1)

	global temp_image2
	temp_image2 = resize_cards(f'images/{player2.currentCard}.png')
	player2_label.config(image=temp_image2)

	card_button.config(state='enabled')

def dealNext():
	try :
		if (player1.isWinner(player2.currentCard)):
			player1.win(player2.currentCard)
			player2.lose()
			player1_status_label.config(text=f'WINNER :-) {player1.showHand()}')
			player2_status_label.config(text=f'LOSER :-( {player2.showHand()}')
		else:
			player2.win(player1.currentCard)
			player1.lose()
			player2_status_label.config(text=f'WINNER :-) {player2.showHand()}')
			player1_status_label.config(text=f'LOSER :-( {player1.showHand()}')


		player1.draw(deck)
		player2.draw(deck)

		global temp_image1
		temp_image1 = resize_cards(f'images/{player1.currentCard}.png')
		player1_label.config(image=temp_image1)

		global temp_image2
		temp_image2 = resize_cards(f'images/{player2.currentCard}.png')
		player2_label.config(image=temp_image2)

		root.title(f'{len(deck)} Cards Left')
	except Exception as e:
		print(f"An exception occurred: {str(e)}")
		card_button.config(state='disabled')
		root.title('GAME OVER')

deck = Deck()

player1 = Player('First')
player2 = Player('Second')

my_frame = tk.Frame(root, bg="green")
my_frame.pack(pady=20)

player1_frame = tk.LabelFrame(my_frame, text=player1.sayHello(), bd=0)
player1_frame.grid(row=0, column=0, padx=20, ipadx=20)

player2_frame = tk.LabelFrame(my_frame, text=player2.sayHello(), bd=0)
player2_frame.grid(row=0, column=1, ipadx=20)

player1_label = tk.Label(player1_frame, text='')
player1_label.pack(pady=20)

player1_status_label = tk.Label(player1_frame, text='status')
player1_status_label.pack(pady=10)

player2_label = tk.Label(player2_frame, text='')
player2_label.pack(pady=20)

player2_status_label = tk.Label(player2_frame, text='status')
player2_status_label.pack(pady=10)

start_button = tk.Button(root, text="Start game", font=("Helvetica", 14), command=startGame)
start_button.pack(pady=20)

card_button = tk.Button(root, text="Get Cards", font=("Helvetica", 14), command=dealNext)
card_button.pack(pady=20)

root.mainloop()