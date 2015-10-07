import Ember from 'ember';

export default function getObject(store, model, primaryKey) {
  var object = store.peekRecord(model, primaryKey);
  if (Ember.isEmpty(object)) {
    var object = store.findRecord(model, primaryKey);
  }
  return object;
}
