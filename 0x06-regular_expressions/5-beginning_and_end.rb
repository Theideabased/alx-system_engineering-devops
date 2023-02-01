#!/usr/bin/env ruby
# This will search text that start with 'h' and ended with 'n'
puts ARGV[0].scan(/^h.n$/).join
