import DS from 'ember-data';
import BaseModelMixin from 'emdj/mixins/base-model';

var File = DS.Model.extend(BaseModelMixin, {
  pages: DS.hasMany("page"),
  project: DS.belongsTo('project', {
    inverse: 'files'
  })
});
export default File;
