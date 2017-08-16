class Event < ActiveRecord::Base
  belongs_to :user, required: true
  has_many :discussions
  has_many :attending_events, dependent: :destroy
  has_many :users, through: :attending_events

  validate :name, :date, :city, :state, presence: true

end