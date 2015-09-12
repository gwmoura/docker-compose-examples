FROM ruby:2.2.2
RUN mkdir /src
WORKDIR /src
ADD ./src/Gemfile /src/
RUN bundle install
ADD ./src/ /src/