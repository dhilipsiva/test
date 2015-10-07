import Ember from 'ember';
import getObject from 'emdj/utils/get-object'

export default Ember.Mixin.create({
  getObject: function(model, primaryKey){
    return getObject(this.store, model, primaryKey);
  }
});
