import Ember from 'ember';
import BaseModelMixin from '../../../mixins/base-model';
import { module, test } from 'qunit';

module('Unit | Mixin | base model');

// Replace this with your real tests.
test('it works', function(assert) {
  var BaseModelObject = Ember.Object.extend(BaseModelMixin);
  var subject = BaseModelObject.create();
  assert.ok(subject);
});
