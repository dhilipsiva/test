import DS from 'ember-data';
import BaseModelMixin from 'emdj/mixins/base-model';

var Page = DS.Model.extend(BaseModelMixin, {
  file: DS.belongsTo('file', {
    inverse: 'pages'
  })
});
export default Page;

