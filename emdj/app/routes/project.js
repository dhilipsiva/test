import Ember from 'ember';
import GetObjectMixin from 'emdj/mixins/get-object';

export default Ember.Route.extend(GetObjectMixin, {
  model: function(params) {
    return this.getObject('project', params.project_uuid);
  }
});
