#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Basic example of pylive usage: scan a Live set, trigger a clip,
# and modulate some device parameters.
#------------------------------------------------------------------------
import live
import random

#------------------------------------------------------------------------
# Scan the set's contents and set its tempo to 110bpm.
#------------------------------------------------------------------------
set = live.Set()
set.scan(scan_clip_names = True, scan_devices = True)
set.tempo = 110.0

#------------------------------------------------------------------------
# Each Set contains a list of Track objects.
#------------------------------------------------------------------------
track = set.tracks[0]
print("Track name %s" % track.name)

#------------------------------------------------------------------------
# Each Track contains a list of Clip objects.
#------------------------------------------------------------------------
clip = track.clips[0]
print("Clip name %s, length %d beats" % (clip.name, clip.length))
clip.play()

#------------------------------------------------------------------------
# We can determine our internal timing based on Live's timeline using
# Set.wait_for_next_beat(), and trigger clips accordingly.
#------------------------------------------------------------------------
set.wait_for_next_beat()
clip.get_next_clip().play()

#------------------------------------------------------------------------
# Now let's modulate the parameters of a Device object.
#------------------------------------------------------------------------
# device = track.devices[0]
# parameter = random.choice(device.parameters)
# parameter.value = random.uniform(parameter.minimum, parameter.maximum)