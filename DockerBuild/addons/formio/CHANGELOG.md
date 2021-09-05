# Changelog

### 8.33

- Fix warning: `Two fields (formio_version_name, formio_version_id) of formio.builder() have the same label.`
- Fix warning: `The domain term '('formio_version_id', '=', [py:int])' should use the 'in' or 'not in' operator.`

### 8.32

- New feature for public Form in Wizard mode: on next page perform a save draft.\
  This is a (boolean/checkbox) setting in the Builder.

### 8.31

- Add *formio.js* (library project) license file, also with GitHub downloader/installer.\
  *formio.js* - https://github.com/formio/formio.js

### 8.30

- Improve the submitDone redirect feature.\
  Config should be explicit; don't wait on timeout and then redirect anymore.

### 8.29

- Add session variable `formio_last_form_uuid` upon POST `/formio/public/form/create`.

### 8.28

- Correct misunderstanding, leftover names regarding the formio.js library.

### 8.27

- Fix bug/regression in `formio.form` (create) `_prepare_create_vals` and `write`, due to timezone feature added in version 8.25

### 8.26

- Fix bug/regression in `formio.form` (create) `_prepare_create_vals`, due to timezone feature added in version 8.25

### 8.25

- Store timezone (from the partner) of the Form submission.

### 8.24

- Add translation for the alert message(s), in top of the Form.
  - Translated for language codes: nl, nl_BE, pt_BR, zh_CN.
  - Relates to: https://github.com/formio/formio.js/issues/3105, https://github.com/formio/formio.js/issues/2627
- Add translation for the submitError message, near submit button of the Form.
  - Translated for language codes: nl, nl_BE, pt_BR, zh_CN.

### 8.23

- Fix: Nested components (eg inside datagrid, editgrid) **Data Source URL**
- Prefix the Data Source URL with the Odoo controller endpoint, with format: `/formio/form/<string:uuid>/data/?query...`

### 8.22

- Fix: Language determination in Public Form (also used by the `website_formio` module).
- Improve JsonRPC client using Odoo's JsonRpc internals (from `web.ajax`).

### 8.21

- Form Builder (UI) improvement: Extend width to 95% of container (viewport), which was too narrow before.

### 8.20

- Fix: Ordering of "formio.js version" in (Many2one) selection fields e.g. in Form and Config settings.

### 8.19

- Fix: Translations didn't worked, due to regression by latest change in `formio.builder` function `i18n_translations`

### 8.18

- Fix: Issue in Form (form-view) searching Builder(s) really didn't worked properly.\
  Technical details:\
  This change addresses the `formio.builder`, adding the `search` method for the computed field `display_name_full` which is used as `_rec_name`.

### 8.17

- Fix: Error when uninstall and installing again. `Record does not exist or has been deleted. (Record: formio.builder.js.options(1,), User: 2)`\
  Uninstall now deletes the system parameter (record) with key `formio.default_builder_js_options_id`

### 8.16

- New feature: Grant copy Forms persmission (button), also in portal, configured by Form Builder.\
  It's also possible to configure whether the Form should be copied and merged into the latest/current Form Builder schema (design).

### 8.15

- Removed rigorous record rule `ir_attachment_unlink_formio_form` (Attachments of completed Forms can't be deleted).\
  This was intended, now moved and improved in the module `formio_storage_filestore`.

### 8.14

- Fix: delete and cancel actions of Form in the portal.

### 8.13

- Forms app/module Category.
- In User form, ensure User Groups in dropdown/select instead of checkboxes.

### 8.12

- Form (field) Title is required and indexed.

### 8.11

- Fix singleton error, when matching multiple Partners by email in the Form (e.g. for following and report emails).\
  PR [\#109](https://github.com/novacode-nl/odoo-formio/pull/109)
- Schedule Activity (on Form) if found multiple Partners with same email submitted in the Form.

### 8.10

- JavaScript: Set the `baseUrl` (value: `window.location.href`) on the (formio.js) Formio object.\
  The `baseUrl` is the Form it's `<iframe src=.../>` attribute.\
  This can be used in other (integration) modules e.g. for security/access checking etc.

### 8.9

- Fix server crashing due to request unbound error, while installing or updating module.\
  Bug has been introduced in version 8.7, `formio.builder` function `_compute_public_url` of computed field `public_url`.

### 8.8

- In model `ir.attachment` define the relational field `formio_form_id = fields.Many2one('formio.form')`\
  Can be used for all kinds of integration e.g. files upload storage.

### 8.7

- In Form Builder show URL/link to public create Form (e.g. to embed, share).

### 8.6

- Fix: Language determination in Public Form (also used by `website_formio` module).\
  PR [\#101](https://github.com/novacode-nl/odoo-formio/pull/101)

### 8.5

- Fix (4): language switcher buttons and translations in public Forms (also used by `website_formio` module).\
  Convert the Odoo language code (underscore "_") to Formio (formio.js) JavaScript's i18n expected IETF code (hyphen "-").\
  PR: [\#100](https://github.com/novacode-nl/odoo-formio/pull/100)

### 8.4

- Fix: formio.js version updates in Windows environments are not available.\
  PR: [\#92](https://github.com/novacode-nl/odoo-formio/pull/92)

### 8.3

- Fix (3): language switcher buttons and translations in Form Builder and Forms.\
  Convert the Odoo language code (underscore "_") to Formio (formio.js) JavaScript's i18n expected IETF code (hyphen "-").\
  Issues: [\#91](https://github.com/novacode-nl/odoo-formio/issues/91), [\#93](https://github.com/novacode-nl/odoo-formio/issues/93), [\#95](https://github.com/novacode-nl/odoo-formio/issues/95)

### 8.2

- Fix (2): language switcher buttons and translations in Form Builder and Forms.\
  Issues: [\#91](https://github.com/novacode-nl/odoo-formio/issues/91), [\#93](https://github.com/novacode-nl/odoo-formio/issues/93)

### 8.1

- Fix (1): language switcher buttons in Form Builder and Forms.\
  Shown languages (buttons) are determined by configured languages in the Form Builder.\
  Issues: [\#91](https://github.com/novacode-nl/odoo-formio/issues/91), [\#93](https://github.com/novacode-nl/odoo-formio/issues/93)
- Add translations pt_BR: Portuguese (BR)

### 8.0

- Rename the App and other UI parts (titles, labels) to "Forms"

### 7.9

- Fix: obtaining the latest GitHub 30 release versions often get (HTTP) 403 errors.\
  Adds a **GitHub personal access token** in the Settings, to get a higher rate limit.

### 7.8

- Fix: Forms should be accessible when user belongs to both groups: *User: Assigned forms* and *User: All forms*
  Group *User: All forms* takes precedence over *User: Assigned forms*.

### 7.7

- Translatable (multilingual) public Forms, with language-switcher buttons.\
  This addresses issues: [\#58](https://github.com/novacode-nl/odoo-formio/issues/58), [\#47](https://github.com/novacode-nl/odoo-formio/issues/47)
- Translatable (multilingual) Form Builder, with language-switcher buttons.

### 7.6

- New feature: specify Form Builder Javascript options API/argument.\
  Form Builder JavaScript options can be specified in the form-view (tab) and shall be stored in `formio.builder` record.\
  Default (global) JavasScript options can be specified in the Forms Settings, which are by default loaded while creating a Form Builder.\
  For example, the Form Builder editForm File component options: https://github.com/formio/formio.js/tree/master/src/components/file/editForm

### 7.5

- Fix Form Builder save (JavaScript event handler).\
  Use the event handler its argument (schema/components) instead of `self.schema` (scary change/bug)\
  Issue: [\#66](https://github.com/novacode-nl/odoo-formio/issues/66)

### 7.4

- Implemented Form Builder `copy()` method, which previously was blocked / not possible. This due to unique contraint validation on fields `name` and `version`.\
  Upon copy, the new Form Builder its name (field value) shall be suffixed with a datetime-stamp.

### 7.3

- Configurable redirect, after (submit) submission of Portal and Public (website) Form:
  - Configuration in Form Builder
  - Handle whether to redirect or reload (new) Form.
- Redirect after Submit-done configuration for Portal and Public (website) Forms.

### 7.2

- Fix Form not loaded. Javascript workaround (known) browser incompatibility errors.
  - Mac: Safari 12.x, 13.1
  - iOS: Safari\
  Issues:
  - Safari 13.1 on Mac experienced error: 1unexpected token '='. expected an opening '(' before a method's parameter list`
  - iOS issue solved, but details not debugged. Dev Tools not ready/present in iOS browsers.

### 7.1

- Fix frontend JavaScript: Execute `loadForm()` after the DOM has been `mounted()`, not upon (async) `willStart()`.\
  (This of course failed to bootstrap the (formio) App when the DOM wasn't loaded, which results in nothing).
- Improve frontend JavaScript: Add `initForm()` hook and implement specific constructor/object properties in the App classes (backend_app.js, public_app.js, public_create_app.js).\
  E.g. to set `config_url = '/formio/public/form/' + this.form_uuid + '/config';`

### 7.0
- Frontend rebuild with **Owl (Odoo Javascript framework)** - Form Builder and Form:
  - Use the Owl - https://odoo.github.io/owl - JavaScript framework, to abstract the Form component into a Component class.
  - JavaScript modules (export/import) to bind the Owl classes into specific backend and public Form (Owl) Apps.
  - This also breaks/ends support for Internet Explorer, which is already published EOL.
- Changed some endpoint URLs (to improve URL conventions).

### 6.1

- Version GitHub tags: Add scheduled action (ir.cron daily) which checks and registers new client/library Versions (GitHub tags).
- Version GitHub tags: Add field "Installed on", which stores the installation datetime.
- Version GitHub tags: Highlight installed version records with color (success/green).

### 6.0

- New feature: formio.js (client/library) Version Checker, Importer and Installer tool.\
  Now administrators can check, import (from GitHub) and install new releases/versions by a single click in Odoo.\
  Soon a scheduled Cron action shall be implemeneted which does the (default daily) checking and importing.
- New feature: Configuration setting to specify the default formio.js (client/library) Version for any new Form Builder.

### 5.3

- New Components API feature: create a Partner after Form submission. Possibility to add the Partner to Followers of the Form record.
  Configuration in Form Builder: Partner field/component (email, name), Add to Followers (checkbox/boolean).

### 5.2

- Add Form Builder UUID (field).
- Data migration: update all `formio_builder` records, set UUID (field) with generated value.
- Change the public Form loading and submit (URLs, handling) from ID to UUID.\
  This slightly protects from abuse of public Forms (some obfuscation of the real id).
  Issue: [\#46](https://github.com/novacode-nl/odoo-formio/issues/46)

### 5.1

- New tab *Components API* in Form Builder form-view.

### 5.0

- Public Forms - Access configuration and check (by interval expiration settings: minutes, hours, days).
- Public Forms - Improvements in (web)controller, templating and JavaScript:
  - Split up JavaScript files, which implement the Form handling (backend, public, public new).
  - This change is subjected to redundant code (DRY), but works for now and shall be addressed by using a JavaScript framework (probably Owl).
- Change `formio.form` toplevel URLs: remove the `/root` suffix.\
  This was introduced in 1.8. Seems not to be an issue anymore.

### 4.5

- Add optional UUID (field) into Forms list view.

### 4.4

- Change 4.3 implementation (`>final_res` fields), which was rather confusing:
  - Remove the `final_res_model`, `final_res_id` fields.
  - Instead: in model `formio.form` added fields `initial_res_model_id`, `initial_res_id`.
  - These fields store the initial (referenced) resource record. So swapping the `res_model_id` and `res_id` afterwards is supported, for specific implementation requirements.
  - Add migration to update `formio_form` records: `res_model_id` (determined by `formio_builder`), copy `res_id` to `initial_res_id`.

### 4.3

- In model `formio.form` added fields `final_res_model`, `final_res_id`.\
  These fields can be used to swap the (referenced) resource record, for specific implementation requirements.
- In model `formio.builder` added field `res_model`, which represents the technical model-name.

### 4.2

- In the **create Form (form-view)** by default provide only Form Builders **without Resource-model** in the **Form Builder drop-down field**.\
  Specific modules extend this (domain) filter to add appropriate Form Builders related to the (active) Resource-model - e.g. formio_sale, formio_stock.

### 4.1

- Improvement: ETL Odoo (resource) data into Form, requires to bypass access control on the target/resource model. (Use `sudo` here).

### 4.0

- Basic setup to deploy/share **public Forms**, by a setting (checkbox) in Form Builder.
- Implement **sequence field** in **Form**. Usefull when storing and listing forms in an ordered way.
- New setting (in Form Builder) which instructs the **Form** whether to **show/hide** the **UUID** in Form footer.
- **Store** those **show/hide** setting fields in the **Form**, instead of joining its relational Builder value (in readonly mode).
- **Improvements in tree/list and form views** regarding Form and Builder.

### 3.7

- New setting (in Form Builder) which instructs the Form whether to **show/hide** the **Title**.
- Moved the Form Title from the main HTML-document into the embedded document (iframe).\
  This improves the embedded Form experience.

### 3.6
- New settings (in Form Builder) which instructs the Form whether to **show/hide** some metadata: **Assigned user, Submission user &amp; date, ID, State**.\
  The default is to show all these metadata fields (for backwards compatibility and no data migration needed).
- Import formio.js version 3.x assets and bootstrap (CSS) instead of CDN.
- Fix silly Javascript bug: `_.extend` (underscore.js ain't loaded here). Use jQuery extend.
- Add help text regarding issue with (formio.js) and `view_as_html` setting https://github.com/formio/formio.js/issues/1545

### 3.5

- Add formio.js **v4.9.26** assets `https://github.com/formio/formio.js/releases/tag/v4.9.26`
- User in group *"Forms Admin"* can edit the Form it's submission data, for a new Form (if ain't stored).

### 3.4

- Don't override provided vals in `formio.form` function `_prepare_create_vals()`.

### 3.3

- New feature: ETL Odoo (resource) data into Form.\
  Supported fields:
  - Scalar fields e.g. Char, Text, Integer, Boolean, Date, Datetime
  - Many2one field (load it's leaf/scalar field)
  - One2many field, supported by formio.js Datagrid component

### 3.2

- Optional configuration to allow specific User Group(s) to force update of a **Form state** field (draft, complete, cancel) e.g. by buttons.\
  Feature/issue: [\#36](https://github.com/novacode-nl/odoo-formio/issues/36)

### 3.1

- Fix portal iframe (height) resizing issue [\#35](https://github.com/novacode-nl/odoo-formio/issues/35)

### 3.0

- Changed the way **Resource Fields** are determined and stored. Not by dependent/computed fields anymore, which caused all kind of troubles.\
  Affected fields: `res_name`, `res_info`, `res_act_window_url` and `res_partner_id`.\
  **!! CAUTION, BEFORE UPGRADE: Test first and be sure all Forms data (regarding these fields) has been migrated properly.**

### 2.3

- Form Builder layout improvements: full width, remove horizontal scrollbar.

### 2.2

- Fix (workaround) to solve form height-resizing issues [\#20](https://github.com/novacode-nl/odoo-formio/issues/20)

### 2.1

- Add formio.js **v4.9.23** assets `(https://github.com/formio/formio.js/releases/tag/v4.9.23)`
- Remove formio.js "latest" version (CDN URLs). Requests from CDN caused time-outs.

### 2.0

- Odoo formio **view types** for Builder and Form. Finally one can switch view types (form, formio) within the window action.
- Moved the so-called *Form dock* (info bar) into the iframe. This updates the info on a (iframe) window reload.
- Remove the *submit done url* implementation, which is useless in a backend usage/context.
- Other improvements and simplification.

### 1.10

- Extend `formio.form create` methods with `_prepare_create_vals` method, which in turn specific modules could call to assign field `vals`.
- Fix method `compute_res_fields` which stores fields regarding the resource model (made possible by change in former point).

### 1.9

- Computed fields regarding resource model: Store res_name and res_partner_id. Change dependent compute method.
- Add (related) field submission partner.

### 1.8

- Change URLs and controllers FROM `/formio/form/<action>/<string:uuid>` URLs TO `/formio/form/<string:uuid>/<action>`.\
  This solves issues regarding relative URLs from a Javascript perspective (components). The UUID was stripped by the Javascript client lib.\
  Should solve: [\#11](https://github.com/novacode-nl/odoo-formio/issues/11)
- Remove 2 legacy (obsolete) controller methods for routes: `/formio/form/<string:uuid>` and `/formio/builder/<int:builder_id>`

### 1.7

- Prevent Javascript clashes between Odoo and formio.js. Hence remove all Odoo Javascript (assets) loading in the formio.js iframe.
- Add and load standalone JsonRPC client.

### 1.6

- Portal: Improved (refactored) controller layout values method.
- Portal: form buttons now keep query-params.

### 1.5

- Demo Builder: Save as Draft (button).
- Form update to **Draft** fix (workaround). Remove `submission_data['submit']`.

### 1.4

- Include and serve the formio.js library assets (JS, CSS) within the module. Don't use CDN anymore.
- Click button to display the **Form Builder** in **Full Screen**.

### 1.3

- Portal: Improved (refactored) controller layout values method.
- Portal: form buttons now keep query-params.

### 1.2

- Rename (consistency) Builder form-view id/ref: from `view_formio_builder` to `view_formio_builder_form`.

### 1.1

- Possible "Resource model(s)" needs to be registered from sub-modules e.g. formio_sale.\
  Just choosing from all models is useless and confuses the user about its functionality.

### 1.0

- Form embedded in iframe. This avoids clashes (Javascript and CSS) between Odoo and formio.js.
- Redesign of templates

### 0.16

- Search filters on Form Builder and Forms.
- Assign a user (owner/author/designer) to a Form Builder.

### 0.15

- Change default forms view to list.
- Improve forms kanban to group by state.

### 0.14

- Form Builder versioning. Also create a new Builder version-record (from existing one).

### 0.13

- Form Builder states: Draft (in design), Current (published) and Obsolete (unpublished).

### 0.12

- Redesign of Builder and Form templates. A simplification and improvement.
- Hopefully fixed enough styling issues due to Bootstrap 4 VS 3 in Odoo and loaded JS Form (Builder).
- Other small improvements

### 0.11

- Include new formio.js versions and assets (3.27.3, 4.0.8)
- Add recommendation into the description of the "latest" formio.js version.

### 0.10

- Translation system for Form labels, placeholders etc.
- Language selector on Form.

### 0.9

- Simple Form wizard (is a Form rendering/display mode).

### 0.8

- Access-check improvements.
- UI improvements.
- Dutch translations.

### 0.7

- Dropdown button in Portal, to add and fill-in new Form(s).

### 0.6

- Form state (Pending, In Progress, Complete, Canceled).
- Form is readonly if state is Complete or Canceled.

### 0.5

- Form invitation mail.
- Improvements regarding form assignment (user filter).

### 0.4

- Portal User can use forms.
- Restrict access to assigned forms (Portal User, Internal User).

### 0.3

- Translations system to manage the translatable terms and load into the form.

### 0.2

- formio.js (library: JS, CSS) version management and loading.

### 0.1

Initial version.
