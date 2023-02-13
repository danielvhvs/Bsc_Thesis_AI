# Folder with the sound files
sound_folder$ = "./question_sentences_test"

# List of all the sound file names
file_list$ = listFiles(sound_folder$)

# Create a text file to store the results
createFile: "pitch_data_questions.txt"

interval_length = 0.1
time = 0

# Loop over the sound files
for i to length(file_list$#)
	# Load the sound file
	Read from file: sound_folder$ + "/" + file_list$#[i]
	
	# Select sound file object
	selectObject: "Sound " + file_list$#[i]
	
	# Extract pitch information -time step, -pitch floor, -pitch ceiling
	To Pitch: 0, 75, 600
	
	# Select pitch object that was just created
	selectObject: "Pitch " + file_list$#[i]
	
	# loop over the whole length of the sound, 0,0
	while time <= Get end time: 0, 0
		# Get pitch at time
		pitch = Get value at time: time, "Hertz", "Linear"
		# write pitch and time to file
		appendFile: "pitch_data_questions.txt", time +" " + pitch + " "
		# increase time
		time = time + interval_length
	endwhile
	# Go to next line in text file
	appendFile: "pitch_data_questions.txt", newline
endfor

# End of Praat script

