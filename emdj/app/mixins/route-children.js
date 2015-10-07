import Ember from 'ember';

export default Ember.Mixin.create({
  afterModel: function(model, transition){
    model.loadChildren();
  }
});
