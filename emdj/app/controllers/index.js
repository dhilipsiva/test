import Ember from 'ember';

export default Ember.Controller.extend({
  projects: (function(){
    return this.store.findAll('project');
  }).property()
});
