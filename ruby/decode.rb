# Script to decode Base64 text
# Note that Base64.decode64 ignores characters outside the base alphabet
# see Ruby docs: https://ruby-doc.org/3.0.6/stdlibs/base64/Base64.html
require 'base64'

encoded_string = ARGV[0]

decoded_string = Base64.decode64(encoded_string)

puts decoded_string