import Ember from 'ember';
import GetObjectMixin from 'emdj/mixins/get-object';

export default Ember.Route.extend(GetObjectMixin, {
  model: function(params) {
    var project = this.getObject('project', params.project_uuid);
    debugger;
    return project;

  }
});
