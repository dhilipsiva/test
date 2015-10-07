import Ember from 'ember';
import GetObjectMixin from 'emdj/mixins/get-object';
import RouteChildrenMixin from 'emdj/mixins/route-children';

export default Ember.Route.extend(GetObjectMixin, RouteChildrenMixin, {
  model: function(params) {
    return this.getObject('file', params.file_uuid);
  }
});
