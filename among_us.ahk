#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;created by strox - originally for marv bot but can be edited;

^!Ins::			;mute all in channel
	WinActivate, ahk_exe Discord.exe
	SendInput, $mutechannel{Up}{Enter}
	sleep, 100
	Send, !{Esc}
	return
	
^!Home::			;unmute all in channel
	WinActivate, ahk_exe Discord.exe
	SendInput, $unmutechannel{Up}{Enter}
	sleep, 100
	Send, !{Esc}
	return
	
return

; the "-" is the prefix that the bot uses, this can be edited at will; entire commands too
; ^! corresponds to CONTROL + ALT 
; Numpad** correspond to a number on the numpad; you change all the input here https://autohotkey.com/docs/KeyList.htm