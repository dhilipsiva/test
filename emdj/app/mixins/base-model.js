import Ember from 'ember';
import DS from 'ember-data';

var BaseModelMixin = Ember.Mixin.create({
  name: DS.attr('string'),
  uuid: DS.attr('string')
});

export default BaseModelMixin;
