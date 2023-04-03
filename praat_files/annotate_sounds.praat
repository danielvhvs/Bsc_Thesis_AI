
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
	foundStart = 0
	foundEnd = 0
	while time <= endTime and foundStart = 0
		# Get pitch at time
		pitch = Get value at time: time, "Hertz", "Linear"
		if foundStart = 0 and pitch <> undefined
			foundStart = 1
			startSound = time	
		endif
		# increase time
		time = time + interval_length
	endwhile
	
	time = Get end time
	time = time - 0.01
	while time >= 0 and foundEnd = 0
		# Get pitch at time
		pitch = Get value at time: time, "Hertz", "Linear"
		if foundEnd = 0 and pitch <> undefined
			foundEnd = 1
			endSound = time	
		endif
		# increase time
		time = time - interval_length
	endwhile
	appendFileLine: "sound_intervalRanges.txt", string$ (startSound) + " " + string$ (endSound)
	
	selectObject: "Sound " + filename$
	To TextGrid... "sentence" ""
	selectObject: "TextGrid " + filename$

	Insert boundary... 1 startSound
	Insert boundary... 1 (startSound+0.5)
	Insert boundary... 1 endSound
	Insert boundary... 1 (endSound-0.5)
	
	Set interval text... 1 1 silence
	Set interval text... 1 2 start
	Set interval text... 1 3 middle
	Set interval text... 1 4 end
	Set interval text... 1 5 silence
endfor


