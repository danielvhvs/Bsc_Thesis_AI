
form
  sentence Directory ./question_sentences_test/
endform

Create Strings as file list... list 'directory$'*
numberOfFiles = Get number of strings
for ifile to numberOfFiles
	filename$ = Get string... ifile
		# You can add some filename extensions that you want to be excluded to the next line.
		if right$ (filename$, 4) <> ".doc" and right$ (filename$, 4) <> ".xls" and right$ (filename$, 4) <> ".XLS" and right$ (filename$, 4) <> ".TXT" and right$ (filename$, 4) <> ".txt" and right$ (filename$, 4) <> ".dat" and right$ (filename$, 4) <> ".DAT"
			Read from file... 'directory$''filename$'
		endif
	select Strings list
endfor

interval_length = 0.01

for i to numberOfFiles
	# Select sound file object
	select Strings list
	filename$ = Get string... i
	idxdot = index(filename$, ".")-1
	filename$ = left$ (filename$,idxdot)
	selectObject: "Sound " + filename$
	
	# Extract pitch information -time step, -pitch floor, -pitch ceiling
	To Pitch: 0, 75, 600
	
	# Select pitch object that was just created
	selectObject: "Pitch " + filename$
	
	time = 0
	endTime = Get end time
	# loop over the whole length of the sound, 0,0
	while time <= endTime
		# Get pitch at time
		pitch = Get value at time: time, "Hertz", "Linear"
		# write pitch and time to file
		appendFile: "pitch_data_questions.txt", string$ (time) +" " + string$ (pitch) + " "
		# increase time
		time = time + interval_length
	endwhile
	# Go to next line in text file
	appendFileLine: "pitch_data_questions.txt", ""
endfor

# End of Praat script

