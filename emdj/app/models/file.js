import DS from 'ember-data';
import BaseModelMixin from 'emdj/mixins/base-model';
import ChildrenLoaderMixin from 'emdj/mixins/children-loader';

var File = DS.Model.extend(ChildrenLoaderMixin, BaseModelMixin, {
  children: "page",
  pages: DS.hasMany("page"),
  project: DS.belongsTo('project', {
    inverse: 'files'
  })
});
export default File;
