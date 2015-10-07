import DS from 'ember-data';
import BaseModelMixin from 'emdj/mixins/base-model';
import ChildrenLoaderMixin from 'emdj/mixins/children-loader';

var Project = DS.Model.extend(ChildrenLoaderMixin, BaseModelMixin, {
  children: "file",
  files: DS.hasMany("file")
});

export default Project;
