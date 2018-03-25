#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Sharath R  - 3/18/18

import os, boto3

# setup defaults
defaultRegion = 'us-east-1'
defaultUrl = 'https://polly.us-east-1.amazonaws.com'

# function for connecting to Amazon Polly
def connectToPolly(regionName=defaultRegion, endpointUrl=defaultUrl):
    return boto3.client('polly', region_name=regionName, endpoint_url=endpointUrl)

# generic function for text-to-speech and play speech mp3
def speak(polly, text, format='mp3', voice='Joanna'):
    resp = polly.synthesize_speech(OutputFormat=format, Text=text, VoiceId=voice)
    soundfile = open('/tmp/sound.mp3', 'w')
    soundBytes = resp['AudioStream'].read()
    soundfile.write(soundBytes)
    soundfile.close()
    os.system('afplay /tmp/sound.mp3')  
    os.remove('/tmp/sound.mp3')

# now connect to Polly
polly = connectToPolly()

# speak a sentence 
speak(polly, "Hi! I'm Joan