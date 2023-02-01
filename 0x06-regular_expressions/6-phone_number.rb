#!/usr/bin/env ruby
# This expression will show only 10 digit number
puts ARGV[0].scan(/^\d(10, 10)$/).join
