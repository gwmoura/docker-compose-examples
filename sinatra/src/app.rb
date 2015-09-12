require 'sinatra'
require "sinatra/reloader" if development?

set :bind, '0.0.0.0'
set :port, 3000

get '/' do
  "I' am Online :D"
end

get '/contact' do
  "Contact Page?"
end

get '/ping/:times' do
  times = params['times'].to_i
  
  content = ''
  times.times do |n| 
    content+="#{n} pong<br/>"
  end
  content
end