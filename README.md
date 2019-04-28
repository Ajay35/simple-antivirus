Project following file structure:

source--
	main.py
	algorithm.py
	docker_helper.py
	utility.py
	update.py (Works on machine where local FTP server is configured)
	data (Directory)
		--exelogs (Directory) logs of jar file after scanning will appear here.
		--txtlogs (Directory) logs of text file after scanning will appear here.
		--signatures (Directory) Signatures of viruses are stored here.
		  This directory can be updated if FTP is configured.
		--txtlogs (Directory) sample text test files for signature scan (Path can be this or absolute)
		--exelogs (Directory) sample executable jar files for behavioural scan. (Path can be this relatove or absolute)
		--config.py :file used for paths/messages/errors/commands for necessary for app
			This file need to be edited before exucting the app.

Part 
