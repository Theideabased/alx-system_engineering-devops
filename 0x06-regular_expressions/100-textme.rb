#!/usr/bin/env ruby
# This will read from textme document to get the sender phone number
# the reciever phone number and the flag
puts ARGV[0].scan(/\[from:.*?\]\s\[to:.*?\]\s\[flags:.*?\]/).join(',')
