import mido
from tkinter import filedialog
import sys

# Paramètre de base
MinTimeOffPedal = 0.2
MinTimeOffNote = 0.1
MinTimeOnNote = 0.05
MaxTimeOnNote = 4

def convert(fichier) :
	if len(fichier) > 4 :
		if fichier[-4:] == '.mid' :
			print("Fichier sélectionné :", fichier)
	else :
		print("Aucun fichier n'a été sélectionné.")
		return 0
		
	"""
	# Demande les temps minimums
	MinTimeModif = False
	while not MinTimeModif:

		# Demande la modification des temps minimums
		print("\nMinTimeOffPedal =", MinTimeOffPedal)
		print("MinTimeOffNote  =", MinTimeOffNote)
		print("MinTimeOnNote   =", MinTimeOnNote)
		print("MaxTimeOnNote   =", MaxTimeOnNote)
		ls_PrametreTime = input('\nEcrivez comme suit si vous voulez modifier les temps minimum "0.2 0.1 0.4 6" ou rien si vous voulez en modifier aucune :')
		try:
			
			if not ls_PrametreTime == '':
				# L'écrture de la réponse et convertion en tableau
				ls_PrametreTime = [float(nombre) for nombre in ls_PrametreTime.split()]

				MinTimeOffPedal = ls_PrametreTime[0]
				MinTimeOffNote = ls_PrametreTime[1]
				MinTimeOnNote = ls_PrametreTime[2]
				MaxTimeOnNote = ls_PrametreTime[3]
				
			print("Paramètre enregistré.")
			MinTimeModif = True
			
		except IndexError:
			print('/!\\ Nombre de paramètre incorret.')

		except:
			print('/!\\ Un des paramètres n\'est pas un chiffre.')

	# Liste des instruments dans les fichiers midi
	ls_NameInstrument = (
		"Acoustic Grand Piano",
		"Bright Acoustic Piano",
		"Electric Grand Piano",
		"Honky-tonk Piano",
		"Electric Piano 1",
		"Electric Piano 2",
		"Harpsichord",
		"Clavinet",
		"Celesta",
		"Glockenspiel",
		"Music Box",
		"Vibraphone",
		"Marimba",
		"Xylophone",
		"Tubular Bells",
		"Dulcimer",
		"Drawbar Organ",
		"Percussive Organ",
		"Rock Organ",
		"Church Organ",
		"Reed Organ",
		"Accordion",
		"Harmonica",
		"Tango Accordion",
		"Acoustic Guitar (nylon)",
		"Acoustic Guitar (steel)",
		"Electric Guitar (jazz)",
		"Electric Guitar (clean)",
		"Electric Guitar (muted)",
		"Overdriven Guitar",
		"Distortion Guitar",
		"Guitar Harmonics",
		"Acoustic Bass",
		"Electric Bass (finger)",
		"Electric Bass (pick)",
		"Fretless Bass",
		"Slap Bass 1",
		"Slap Bass 2",
		"Synth Bass 1",
		"Synth Bass 2",
		"Violin",
		"Viola",
		"Cello",
		"Contrabass",
		"Tremolo Strings",
		"Pizzicato Strings",
		"Orchestral Harp",
		"Timpani",
		"String Ensemble 1",
		"String Ensemble 2",
		"Synth Strings 1",
		"Synth Strings 2",
		"Choir Aahs",
		"Voice Oohs",
		"Synth Choir",
		"Orchestra Hit",
		"Trumpet",
		"Trombone",
		"Tuba",
		"Muted Trumpet",
		"French Horn",
		"Brass Section",
		"Synth Brass 1",
		"Synth Brass 2",
		"Soprano Sax",
		"Alto Sax",
		"Tenor Sax",
		"Baritone Sax",
		"Oboe",
		"English Horn",
		"Bassoon",
		"Clarinet",
		"Piccolo",
		"Flute",
		"Recorder",
		"Pan Flute",
		"Blown Bottle",
		"Shakuhachi",
		"Whistle",
		"Ocarina",
		"Lead 1 (square)",
		"Lead 2 (sawtooth)",
		"Lead 3 (calliope)",
		"Lead 4 (chiff)",
		"Lead 5 (charang)",
		"Lead 6 (voice)",
		"Lead 7 (fifths)",
		"Lead 8 (bass + lead)",
		"Pad 1 (new age)",
		"Pad 2 (warm)",
		"Pad 3 (polysynth)",
		"Pad 4 (choir)",
		"Pad 5 (bowed)",
		"Pad 6 (metallic)",
		"Pad 7 (halo)",
		"Pad 8 (sweep)",
		"FX 1 (rain)",
		"FX 2 (soundtrack)",
		"FX 3 (crystal)",
		"FX 4 (atmosphere)",
		"FX 5 (brightness)",
		"FX 6 (goblins)",
		"FX 7 (echoes)",
		"FX 8 (sci-fi)",
		"Sitar",
		"Banjo",
		"Shamisen",
		"Koto",
		"Kalimba",
		"Bagpipe",
		"Fiddle",
		"Shanai",
		"Tinkle Bell",
		"Agogo",
		"Steel Drums",
		"Woodblock",
		"Taiko Drum",
		"Melodic Tom",
		"Synth Drum",
		"Reverse Cymbal",
		"Guitar Fret Noise",
		"Breath Noise",
		"Seashore",
		"Bird Tweet",
		"Telephone Ring",
		"Helicopter",
		"Applause",
		"Gunshot"
	)

	# Va demander à l'utilisateur quelle piste il veut supprimer
	TrackSup = False
	NameInstrument = "[ERROR] No instrument defined"
	while not TrackSup:

		# Affichage de la liste des pistes
		print(' ')
		for i, track in enumerate(midiFileIn.tracks):
			j = 0
			try:
				while not track[j].type == 'program_change':
					j += 1
				NameInstrument = ls_NameInstrument[track[j].program]
			except IndexError:
				pass
			print(i + 1, ')', NameInstrument)

		# Demande la liste des pistes a supprimer
		ls_trackDelete = input('\nEcrivez comme suit si vous voulez supprimer des pistes "1 3 11" ou rien si vous voulez en supprimer aucune :')

		try:
			
			# L'écrture de la réponse et convertion en tableau
			ls_nombresTrack = [int(nombre) for nombre in ls_trackDelete.split()]

			# Trie la liste du plus grand au plus petit
			ls_nombresTrack.sort(reverse=True)

			# Supprime les pistes désignées
			for nombreTrack in ls_nombresTrack:
				if not nombreTrack == '':
					del midiFileIn.tracks[nombreTrack - 1]
					print('la piste', nombreTrack, 'a été supprimée.')

			print(' ')  
			TrackSup = True
			
		except IndexError:
			print('/!\\ La piste', nombreTrack, 'n\'existe pas.')

		except:
			print('/!\\ Le numéro d\'une piste n\'est pas un chiffre.')

	# Verifie si l'utilisateur a supprimé toutes les pistes
	if len(midiFileIn.tracks) == 0:
		print('/!\\ Vous avez supprimé toutes les pistes.')
		sys.exit()
	"""
	
	# Creation d'une liste pour enregistrer les messages (note 20 indique la pédale)
	ls_noteInfo = []
	
	# Lit le fichier midi et on extrait ses données
	midiFileIn = mido.MidiFile(fichier)
	
	# Lancement de la musique et enregistre chaque message à quel temps il est arrivé et aussi avec la pédal
	CurrentTime = 0
	for message in midiFileIn.playNoTime():

		# Calcul du temps du message
		CurrentTime += message.time

		match message.type:

			case 'note_on':
				if message.velocity == 0:
					# C'est un message de désactivation de note
					ls_noteInfo.append([CurrentTime, False, message.note])
				else:
					# C'est un message d'activation de note
					ls_noteInfo.append([CurrentTime, True, message.note])

			case 'note_off':
				# C'est un message de désactivation de note
				ls_noteInfo.append([CurrentTime, False, message.note])

			case 'control_change':
				if message.control == 64:
					if message.value == 0:
						# C'est un message de désactivation de pédale
						ls_noteInfo.append([CurrentTime, False, 20])
					else:
						# C'est un message d'activation de pédale
						ls_noteInfo.append([CurrentTime, True, 20])

	# Analyse des temps dans le ficher Midi et modification des ses temps
	delta = 0
	for cursor in range(len(ls_noteInfo)):
		
		# Si c'est un message d'activation
		if ls_noteInfo[cursor][1]:

			# Verifie si la note n'est pas trop longtemps activée sinon on raccourcit le temps
			# Va chercher en avant une désactivation de la même note
			delta = 0
			while True:
				# A trouvé le message
				if ls_noteInfo[cursor + delta][1] == False and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]:
					# calcul de la difference de temps entre l'activation et la désactivation
					deltaTime = ls_noteInfo[cursor + delta][0] - ls_noteInfo[cursor][0]
					# Modification de la position dans le temps du message de désactivation si la difference de temps est trop grande
					if deltaTime > MaxTimeOnNote:
						ls_noteInfo[cursor + delta][0] -= deltaTime - MaxTimeOnNote
					break
				# Si ce n'est pas le prochain message regarde encore plus en avant
				if not (ls_noteInfo[cursor + delta][1] == False and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]):
					delta += 1
				# S'il est arrivé a la fin du fichier alors il passe au prochain
				if cursor + delta >= len(ls_noteInfo):
					break

		# Si c'est un message de désactivation
		else:

			# Si c'est un message de pédale
			if ls_noteInfo[cursor][2] == 20:

				# Verifie si la pédal est relacher assez long temps pour que elle puisse étouffé les cordes sinon on prevoit du temp       
				# Va chercher en avant une activation de la pédale 
				delta = 0
				while True:
					# A trouvé le message
					if ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == 20:
						# calcul de la difference de temps entre la désactivation et l'activation
						deltaTime = ls_noteInfo[cursor + delta][0] - ls_noteInfo[cursor][0]
						# Modification de la position dans le temps du message d'activation si la difference de temps est trop petite
						if deltaTime < MinTimeOffPedal:
							ls_noteInfo[cursor][0] -= MinTimeOffPedal - deltaTime
						break
					# Si ce n'est pas le prochain message regarde encore plus en avant
					if not (ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == 20):
						delta += 1
					# S'il est arrivé a la fin du fichier alors il passe au prochain calcul de message
					if cursor + delta >= len(ls_noteInfo):
						break

			# Si c'est un message de note
			else:

				# Verifie si la note est relachée assez long temps pour qu'elle puisse retaper les cordes sinon on prevoit du temps
				# Va chercher en avant une activation de la même note 
				delta = 0
				while True:
					# A trouvé le message
					if ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]:
						# calcul de la difference de temps entre la désactivation et l'activation
						deltaTime = ls_noteInfo[cursor + delta][0] - ls_noteInfo[cursor][0]
						# Modification de la position dans le temps du message d'activation si la difference de temps est trop petite
						if deltaTime < MinTimeOffNote:
							ls_noteInfo[cursor][0] -= MinTimeOffNote - deltaTime
						else:
							# Mais sinon aussi verifie si la note est jouée assez long temps pour que le martau arrive à la corde.
							# Va chercher en arrière une activation de la même note
							delta = 0
							while True:
								# A trouvé le message
								if ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]:
									# calcul de la difference de temps entre l'activation et la désactivation
									deltaTime = ls_noteInfo[cursor][0] - ls_noteInfo[cursor + delta][0]
									# Modification de la position dans le temps du message de désactivation si la difference de temps est trop petite
									if deltaTime < MinTimeOnNote:
										ls_noteInfo[cursor][0] += MinTimeOnNote - deltaTime
									break
								# Si ce n'est pas le précédent message regarde encore plus en arrière
								if not (ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]):
									delta -= 1
								# S'il est arrivé au début du fichier alors il passe au prochain calcul de message
								if cursor + delta < 0:
									break
						break
					if not (ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]):
						delta += 1
					# S'il est arrivé a la fin du fichier alors il regarde pour la seconde verification
					if cursor + delta >= len(ls_noteInfo):
						# Qui verifie si la note est jouée assez long temps pour que le martau arrive à la corde.
						# Va chercher en arrière une activation de la même note
						delta = 0
						while True:
							# A trouvé le message
							if ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]:
								# calcul de la difference de temps entre l'activation et la désactivation
								deltaTime = ls_noteInfo[cursor][0] - ls_noteInfo[cursor + delta][0]
								# Modification de la position dans le temps du message de désactivation si la difference de temps est trop petite
								if deltaTime < MinTimeOnNote:
									ls_noteInfo[cursor][0] += MinTimeOnNote - deltaTime
								break
							# Si ce n'est pas le précédent message regarde encore plus en arrière
							if not (ls_noteInfo[cursor + delta][1] and ls_noteInfo[cursor + delta][2] == ls_noteInfo[cursor][2]):
								delta -= 1
							# S'il est arrivé au début du fichier alors il passe au prochain calcul de message
							if cursor + delta < 0:
								break
						break

	ls_noteInfo.sort(key=lambda x: x[0])

	# Arondit les temps à la milli seconde
	for noteInfo in ls_noteInfo:
		noteInfo[0] = round(noteInfo[0], 3)

	# Va chercher le tempo de la musique
	isFind = False
	for track in midiFileIn.tracks:
		if isFind:
			break
		for msg in track:
			if msg.type == 'set_tempo':
				tempo = msg.tempo
				isFind = True
				break

	# Va chercher le message de la time signature de la musique
	isFind = False
	for track in midiFileIn.tracks:
		if isFind:
			break
		for msg in track:
			if msg.type == 'time_signature':
				MessageTimeSignature = msg
				isFind = True
				break

	# set le tick per beat
	ticksPerBeat = 360

	# Réecrit la mémoire ls_noteInfo en un fichier midi

	# Créer une nouvelle piste avec des messages
	track = mido.MidiTrack()

	# Ajouter le message du time signature
	track.append(MessageTimeSignature)

	# Ajouter le message du tempo
	track.append(mido.MetaMessage('set_tempo', tempo=tempo))

	# Ajouter le message qui indique que c'est un piano
	track.append(mido.Message('program_change', program=0))

	# Ajoute les notes dans la track
	for cursor in range(len(ls_noteInfo)):

		# Calcul du temp dans le message
		if cursor == 0:
			deltaTime = 0
		else:
			deltaTime = mido.second2tick(ls_noteInfo[cursor][0] - ls_noteInfo[cursor - 1][0], ticksPerBeat, tempo)

		if ls_noteInfo[cursor][2] == 20:
			if ls_noteInfo[cursor][1]:
				# C'est un message d'activation de pédal
				track.append(mido.Message('control_change', control=64,  value=100, time=deltaTime))
			else:
				# C'est un message de désactivation de pédal
				track.append(mido.Message('control_change', control=64,  value=0, time=deltaTime))
		else:
			if ls_noteInfo[cursor][1]:
				# C'est un message d'activation de note
				track.append(mido.Message('note_on', note=ls_noteInfo[cursor][2],  velocity=100, time=deltaTime))
			else:
				# C'est un message de désactivation de note
				track.append(mido.Message('note_off', note=ls_noteInfo[cursor][2],  velocity=0, time=deltaTime))

	# Ajoute à la fin le message de fin de piste
	track.append(mido.MetaMessage('end_of_track', time=0))

	# Créer un objet MidiFile et ajouter la piste
	midiFileOut = mido.MidiFile() 

	# Set le ticksPerBeat 
	midiFileOut.ticks_per_beat = ticksPerBeat

	# Ajoute la track au fichier midi
	midiFileOut.tracks.append(track)

	# Enregistrer le fichier MIDI
	midiFileOut.save(fichier[:fichier.rfind('.')] + '_Conv.mid')

	print('Midi convertit')
	return 1
