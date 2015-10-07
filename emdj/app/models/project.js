import DS from 'ember-data';
import BaseModelMixin from 'emdj/mixins/base-model';

var Project = DS.Model.extend(BaseModelMixin, {
  files: DS.hasMany("file")
});
export default Project;
