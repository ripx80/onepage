# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OnepageTranslation'
        db.create_table(u'onepage_onepage_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('intro_title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('intro_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('callout_title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('map_title', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('landing_subtitle', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.Onepage'])),
        ))
        db.send_create_signal(u'onepage', ['OnepageTranslation'])

        # Adding unique constraint on 'OnepageTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_onepage_translation', ['language_code', 'master_id'])

        # Adding model 'Onepage'
        db.create_table(u'onepage_onepage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('callout_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('map_link', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=300, null=True, blank=True)),
            ('map_src', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=300, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'onepage', ['Onepage'])

        # Adding model 'ServicesTranslation'
        db.create_table(u'onepage_services_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('service_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.Services'])),
        ))
        db.send_create_signal(u'onepage', ['ServicesTranslation'])

        # Adding unique constraint on 'ServicesTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_services_translation', ['language_code', 'master_id'])

        # Adding model 'Services'
        db.create_table(u'onepage_services', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('display', self.gf('django.db.models.fields.CharField')(default='rocket', max_length=20)),
        ))
        db.send_create_signal(u'onepage', ['Services'])

        # Adding model 'PortfolioTranslation'
        db.create_table(u'onepage_portfolio_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.Portfolio'])),
        ))
        db.send_create_signal(u'onepage', ['PortfolioTranslation'])

        # Adding unique constraint on 'PortfolioTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_portfolio_translation', ['language_code', 'master_id'])

        # Adding model 'Portfolio'
        db.create_table(u'onepage_portfolio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'onepage', ['Portfolio'])

        # Adding model 'Phone'
        db.create_table(u'onepage_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'onepage', ['Phone'])

        # Adding model 'Mail'
        db.create_table(u'onepage_mail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75, db_index=True)),
        ))
        db.send_create_signal(u'onepage', ['Mail'])

        # Adding model 'ContactTranslation'
        db.create_table(u'onepage_contact_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('country', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.Contact'])),
        ))
        db.send_create_signal(u'onepage', ['ContactTranslation'])

        # Adding unique constraint on 'ContactTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_contact_translation', ['language_code', 'master_id'])

        # Adding model 'Contact'
        db.create_table(u'onepage_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('plz', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'onepage', ['Contact'])

        # Adding M2M table for field phone on 'Contact'
        m2m_table_name = db.shorten_name(u'onepage_contact_phone')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'onepage.contact'], null=False)),
            ('phone', models.ForeignKey(orm[u'onepage.phone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'phone_id'])

        # Adding M2M table for field mail on 'Contact'
        m2m_table_name = db.shorten_name(u'onepage_contact_mail')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'onepage.contact'], null=False)),
            ('mail', models.ForeignKey(orm[u'onepage.mail'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'mail_id'])

        # Adding model 'SocialTranslation'
        db.create_table(u'onepage_social_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=250, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.Social'])),
        ))
        db.send_create_signal(u'onepage', ['SocialTranslation'])

        # Adding unique constraint on 'SocialTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_social_translation', ['language_code', 'master_id'])

        # Adding model 'Social'
        db.create_table(u'onepage_social', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('network', self.gf('django.db.models.fields.CharField')(default='facebook', max_length=20)),
        ))
        db.send_create_signal(u'onepage', ['Social'])

        # Adding model 'SiteNoticeTranslation'
        db.create_table(u'onepage_sitenotice_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.SiteNotice'])),
        ))
        db.send_create_signal(u'onepage', ['SiteNoticeTranslation'])

        # Adding unique constraint on 'SiteNoticeTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_sitenotice_translation', ['language_code', 'master_id'])

        # Adding model 'SiteNotice'
        db.create_table(u'onepage_sitenotice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'onepage', ['SiteNotice'])

        # Adding model 'DataPolicyTranslation'
        db.create_table(u'onepage_datapolicy_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['onepage.DataPolicy'])),
        ))
        db.send_create_signal(u'onepage', ['DataPolicyTranslation'])

        # Adding unique constraint on 'DataPolicyTranslation', fields ['language_code', 'master']
        db.create_unique(u'onepage_datapolicy_translation', ['language_code', 'master_id'])

        # Adding model 'DataPolicy'
        db.create_table(u'onepage_datapolicy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'onepage', ['DataPolicy'])

        # Adding model 'News'
        db.create_table(u'onepage_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_update', self.gf('django.db.models.fields.DateField')(auto_now=True, db_index=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=256)),
        ))
        db.send_create_signal(u'onepage', ['News'])


    def backwards(self, orm):
        # Removing unique constraint on 'DataPolicyTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_datapolicy_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SiteNoticeTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_sitenotice_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SocialTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_social_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ContactTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_contact_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PortfolioTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_portfolio_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ServicesTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_services_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'OnepageTranslation', fields ['language_code', 'master']
        db.delete_unique(u'onepage_onepage_translation', ['language_code', 'master_id'])

        # Deleting model 'OnepageTranslation'
        db.delete_table(u'onepage_onepage_translation')

        # Deleting model 'Onepage'
        db.delete_table(u'onepage_onepage')

        # Deleting model 'ServicesTranslation'
        db.delete_table(u'onepage_services_translation')

        # Deleting model 'Services'
        db.delete_table(u'onepage_services')

        # Deleting model 'PortfolioTranslation'
        db.delete_table(u'onepage_portfolio_translation')

        # Deleting model 'Portfolio'
        db.delete_table(u'onepage_portfolio')

        # Deleting model 'Phone'
        db.delete_table(u'onepage_phone')

        # Deleting model 'Mail'
        db.delete_table(u'onepage_mail')

        # Deleting model 'ContactTranslation'
        db.delete_table(u'onepage_contact_translation')

        # Deleting model 'Contact'
        db.delete_table(u'onepage_contact')

        # Removing M2M table for field phone on 'Contact'
        db.delete_table(db.shorten_name(u'onepage_contact_phone'))

        # Removing M2M table for field mail on 'Contact'
        db.delete_table(db.shorten_name(u'onepage_contact_mail'))

        # Deleting model 'SocialTranslation'
        db.delete_table(u'onepage_social_translation')

        # Deleting model 'Social'
        db.delete_table(u'onepage_social')

        # Deleting model 'SiteNoticeTranslation'
        db.delete_table(u'onepage_sitenotice_translation')

        # Deleting model 'SiteNotice'
        db.delete_table(u'onepage_sitenotice')

        # Deleting model 'DataPolicyTranslation'
        db.delete_table(u'onepage_datapolicy_translation')

        # Deleting model 'DataPolicy'
        db.delete_table(u'onepage_datapolicy')

        # Deleting model 'News'
        db.delete_table(u'onepage_news')


    models = {
        u'onepage.contact': {
            'Meta': {'object_name': 'Contact'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'mail': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['onepage.Mail']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['onepage.Phone']", 'null': 'True', 'blank': 'True'}),
            'plz': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'onepage.contacttranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ContactTranslation', 'db_table': "u'onepage_contact_translation'"},
            'city': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.Contact']"}),
            'street': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'onepage.datapolicy': {
            'Meta': {'object_name': 'DataPolicy'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'onepage.datapolicytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'DataPolicyTranslation', 'db_table': "u'onepage_datapolicy_translation'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.DataPolicy']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'})
        },
        u'onepage.mail': {
            'Meta': {'object_name': 'Mail'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'db_index': 'True'})
        },
        u'onepage.news': {
            'Meta': {'ordering': "('-last_update',)", 'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '256'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'onepage.onepage': {
            'Meta': {'object_name': 'Onepage'},
            'callout_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'map_link': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'map_src': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'onepage.onepagetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'OnepageTranslation', 'db_table': "u'onepage_onepage_translation'"},
            'callout_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'intro_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'landing_subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'map_title': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.Onepage']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'onepage.phone': {
            'Meta': {'object_name': 'Phone'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'onepage.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'onepage.portfoliotranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'PortfolioTranslation', 'db_table': "u'onepage_portfolio_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.Portfolio']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'onepage.services': {
            'Meta': {'object_name': 'Services'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'display': ('django.db.models.fields.CharField', [], {'default': "'rocket'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        u'onepage.servicestranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ServicesTranslation', 'db_table': "u'onepage_services_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.Services']"}),
            'service_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'onepage.sitenotice': {
            'Meta': {'object_name': 'SiteNotice'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'onepage.sitenoticetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SiteNoticeTranslation', 'db_table': "u'onepage_sitenotice_translation'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.SiteNotice']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'})
        },
        u'onepage.social': {
            'Meta': {'object_name': 'Social'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'default': "'facebook'", 'max_length': '20'})
        },
        u'onepage.socialtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SocialTranslation', 'db_table': "u'onepage_social_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '250', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['onepage.Social']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        }
    }

    complete_apps = ['onepage']